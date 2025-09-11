import time
import random
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class Room:
    def __init__(self, location: str, status: str = "dirty"):
        self.location = location
        self.status = status  # "dirty" or "clean"

    def __repr__(self):
        return f"Room({self.location},{self.status})"


class Environment(ABC):
    @abstractmethod
    def __init__(self, agent):
        self.agent = agent

    @abstractmethod
    def execute_step(self, n: int = 1):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    def delay(self, seconds: int):
        # environment-level delay between steps (used for scoring every 1 second)
        self._delay = seconds


class Agent(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, env: Environment):
        pass

    @abstractmethod
    def act(self) -> str:
        """
        Should return an action string, e.g. 'clean', 'right', 'left', 'stop'
        """
        pass


# Simple reflex agent (original style)
class SimpleReflexAgent(Agent):
    def __init__(self):
        self.environment: Optional[Environment] = None

    def sense(self, env: Environment):
        # This agent directly stores the environment pointer to read current percept.
        self.environment = env

    def act(self) -> str:
        # Based only on current percept (no history)
        if self.environment is None:
            return "right" 
        current_room = self.environment.current_room()
        if current_room.status == "dirty":
            return "clean"
        # move right if not dirty, else fallback
        # In n-room environment we define 'right' as move forward (increasing index)
        return "right"


# Model-based reflex agent
class ModelBasedReflexAgent(Agent):
    def __init__(self, n_rooms: int, initial_model: Optional[Dict[int, str]] = None, sensors_enabled: bool = True):
        # model: mapping room_index -> status ('dirty' or 'clean' or 'unknown')
        self.n_rooms = n_rooms
        self.model: Dict[int, str] = {i: "unknown" for i in range(n_rooms)}
        if initial_model:
            for k, v in initial_model.items():
                if 0 <= k < n_rooms:
                    self.model[k] = v
        self.current_index = 0
        self.sensors_enabled = sensors_enabled
        self.env: Optional[Environment] = None

    def sense(self, env: Environment):
        # when sensors_enabled, read the true status of current room and update model
        self.env = env
        if not self.sensors_enabled:
            return
        true_room = env.current_room()
        idx = env.current_index
        self.model[idx] = true_room.status

    def act(self) -> str:
        # If we know current room is dirty in model => clean
        if self.model[self.current_index] == "dirty":
            # perform clean and update model optimistically
            self.model[self.current_index] = "clean"
            return "clean"

        # If not dirty or unknown, try to move to next room that model says is dirty
        # find next dirty in model (simple linear search)
        for offset in range(1, self.n_rooms):
            idx = (self.current_index + offset) % self.n_rooms
            if self.model.get(idx, "unknown") == "dirty":
                # decide direction: move right until you reach idx
                return "right"

        # If nothing known as dirty:
        # - If any unknown rooms remain, move right to explore
        if "unknown" in self.model.values():
            return "right"

        # Everything known and clean → stop
        return "stop"


# n-room environment (general)
class NRoomVacuumEnvironment(Environment):
    def __init__(self, agent: Agent, n: int = 2, initial_dirty: Optional[List[int]] = None, delay_seconds: int = 1):
        assert n >= 2, "n must be >= 2"
        self.n = n
        self.rooms: List[Room] = [Room(location=str(i), status="dirty") for i in range(n)]
        if initial_dirty is not None:
            # mark only listed indices dirty; others clean
            for i in range(n):
                self.rooms[i].status = "dirty" if i in initial_dirty else "clean"
        # else keep all dirty
        self.current = 0  # current room index
        self.agent = agent
        # give agent access
        agent.sense(self)
        self.step = 0
        self._delay = delay_seconds
        self.score = 0
        self.max_steps = 10000

    @property
    def current_index(self):
        return self.current

    def current_room(self) -> Room:
        return self.rooms[self.current]

    def display_perception(self):
        r = self.current_room()
        print(f"Step {self.step}: Percept -> [room_index={self.current}, status={r.status}]")

    def display_action(self, action):
        print(f"Step {self.step}: Action -> [{action}]  Score so far: {self.score}")

    def is_done(self) -> bool:
        return all(r.status == "clean" for r in self.rooms)

    def execute_step(self, n: int = 1):
        for _ in range(n):
            if self.step >= self.max_steps:
                print("Reached max steps; stopping.")
                break

            # perception
            self.display_perception()
            # agent senses (may update internal model)
            self.agent.sense(self)
            action = self.agent.act()

            # perform action
            if action == "clean":
                if self.current_room().status == "dirty":
                    self.current_room().status = "clean"
                    self.score += 25  # +25 for cleaning a dirty room
                    print(f"  --> cleaned room {self.current}. +25 points")
                else:
                    print(f"  --> cleaned (no-op) room {self.current}. (room already clean)")

            elif action == "right":
                # move to next index
                self.current = (self.current + 1) % self.n
                self.score -= 1  # -1 for moving
                print(f"  --> moved right to {self.current}. -1 point")

            elif action == "left":
                self.current = (self.current - 1) % self.n
                self.score -= 1
                print(f"  --> moved left to {self.current}. -1 point")

            elif action == "stop":
                print("  --> agent signalled stop.")
                self.step += 1
                # apply per-second penalty for dirty rooms at end of the second
                dirty_count = sum(1 for r in self.rooms if r.status == "dirty")
                if dirty_count:
                    self.score -= 10 * dirty_count
                    print(f"  (end of second) -{10 * dirty_count} for {dirty_count} dirty rooms")
                break

            else:
                print(f"  --> Unknown action '{action}', treating as no-op")

            # end-of-step scoring per requirements: -10 points for each dirty room every second
            dirty_count = sum(1 for r in self.rooms if r.status == "dirty")
            if dirty_count:
                self.score -= 10 * dirty_count
                print(f"  (end of second) -{10 * dirty_count} for {dirty_count} dirty rooms")

            self.step += 1
            self.display_action(action)
            # delay to emulate 1-second scoring interval
            time.sleep(self._delay)

            if self.is_done():
                print("All rooms clean — environment done.")
                break

    def execute_all(self):
        # run until all clean or stop
        while not self.is_done() and self.step < self.max_steps:
            self.execute_step(1)

    def show_rooms(self):
        print("Rooms:", self.rooms)
        print("Score:", self.score)


# Helper: create example envs & tests
def run_two_room_example():
    print("\n=== Two-room example (simple reflex) ===")
    agent = SimpleReflexAgent()
    env = NRoomVacuumEnvironment(agent=agent, n=2, delay_seconds=0)  # set delay 0 for quick demo
    env.max_steps = 20
    env.execute_all()
    env.show_rooms()


def run_three_room_example():
    print("\n=== Three-room example (simple reflex) ===")
    agent = SimpleReflexAgent()
    # make room 0 and 2 dirty, room 1 clean (demonstration)
    env = NRoomVacuumEnvironment(agent=agent, n=3, initial_dirty=[0, 2], delay_seconds=0)
    env.max_steps = 50
    env.execute_all()
    env.show_rooms()


def run_n_room_example(n=5):
    print(f"\n=== {n}-room example (model-based reflex agent) ===")
    # Start with random dirty pattern
    initial_dirty = [i for i in range(n) if random.random() < 0.5]
    agent = ModelBasedReflexAgent(n_rooms=n, initial_model=None, sensors_enabled=True)
    env = NRoomVacuumEnvironment(agent=agent, n=n, initial_dirty=initial_dirty, delay_seconds=0)
    env.max_steps = 200
    env.execute_all()
    env.show_rooms()


def experiment_no_sensors(n=4):
    print("\n=== Experiment: Model-based agent WITHOUT sensors ===")
    # Create initial dirty pattern (we do NOT give this to the agent)
    initial_dirty = [0, 2]  # true dirty rooms
    # Agent's model initially unknown; sensors disabled
    agent = ModelBasedReflexAgent(n_rooms=n, initial_model=None, sensors_enabled=False)
    env = NRoomVacuumEnvironment(agent=agent, n=n, initial_dirty=initial_dirty, delay_seconds=0)
    env.max_steps = 30
    print("True initial dirty rooms:", initial_dirty)
    env.execute_all()
    env.show_rooms()
    print("Agent's internal model after run:", agent.model)


if __name__ == "__main__":
    # run_two_room_example()
    # run_three_room_example()
    # run_n_room_example(3)
    experiment_no_sensors(4)
