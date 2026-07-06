"""
Abstraction — Abstract Base Classes
=======================================
An abstract class defines a contract (method names) without an
implementation. Subclasses MUST implement every @abstractmethod
before they can be instantiated.
"""

from abc import ABC, abstractmethod


class TrainingInstitute(ABC):
    """Abstract class — cannot be instantiated directly."""

    @abstractmethod
    def training(self):
        pass

    @abstractmethod
    def placement(self):
        pass


class Bhagya(TrainingInstitute):
    def training(self):
        print("Trained in: C, C++, Java")

    def placement(self):
        print("Placed via: Java placement drive")


class Suraj(TrainingInstitute):
    def training(self):
        print("Trained in: HTML, C++, Java")

    def placement(self):
        print("Placed via: HTML placement drive")


class Rutuja(TrainingInstitute):
    def training(self):
        print("Trained in: DL, ML")

    def placement(self):
        print("Placed via: Data Science placement drive")


class TicketBookingService(ABC):
    """A second abstraction example — a common interface with very
    different concrete implementations."""

    @abstractmethod
    def book_ticket(self):
        pass


class IRCTC(TicketBookingService):
    def book_ticket(self):
        print("IRCTC: Ticket confirmed.")


class MakeMyTrip(TicketBookingService):
    def book_ticket(self, source, destination, date):
        print(f"MakeMyTrip: Booking from {source} to {destination} on {date}")


if __name__ == "__main__":
    for student in (Bhagya(), Suraj(), Rutuja()):
        student.training()
        student.placement()
        print()

    IRCTC().book_ticket()
    MakeMyTrip().book_ticket("Nashik", "Pune", "2026-08-15")
