"""Classes for melon orders."""
import random
import datetime


class AbstractMelonOrder():
    def __init__ (self,species,qty,order_type,tax):
        self.species = species

        if qty > 100:
            raise TooManyMelonsError


        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        base_price = random.randrange(5, 10)
        now = datetime.datetime.now()

        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4
        return base_price

    def get_total(self,species, order_type):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "Christmas Melons":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3
        if "Splurge pricing":
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty ):
        super().__init__(species, qty,"domestic",0.08)
        """Initialize melon order attributes."""

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international",0.17)
        """Initialize melon order attributes."""

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """ special orders for goverment"""

    def __init__(self,species, qty):
        super().__init__(species,qty, "government",0.0)
        self.passed_inspection = False

    #can't do it this way bc it's not going to feed into the parent intialization method
    # tax = 0.0
    # order_type = "government"
    # passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
    """Error to raise when too many melons are ordered."""

    def __init__(self):
        """Initialize TooManyMelonsError using init method from ValueError."""

        super().__init__("No more than 100 melons!")