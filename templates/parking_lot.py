from metaclass import ABCMeta, abstractmethod

def singelton(class_instance):
    """ decorator method to implement singelton pattern """
    pass

class ParkingSpot:
    """ class for inititalizing parking spot object """

    def __init__(self):
        self.id = None
        self.vehicle_type = None 
        self.vehicle_id = None 
        self.parking_status = None
        
    def park_vehicle(self):
        pass 

    def unpark_vehicle(Self):
        pass 


class IVehicle(metaclass=ABCMeta):
    """ Interface class to intantiate parking_spot object for different types of vehicle objects """

    @staticmethod
    @abstractmethod
    def assign_parking_spot():
        pass


class IParkingStrategy(metaclass=ABCMeta):
    pass 

class RandomParking(IParkingStrategy):
    pass 

class NearEntryParking(IParkingStrategy):
    pass 

class NearExitParking(IParkingStrategy):
    pass

@singelton
class TwoWheeler(IVehicle):
    """ concrete class to intantiate TwoWheeler manager object """

    parking_spots = []

    def assign_parking_spot(gate_number, parking_strategy):
        pass

@singelton
class DMV(IVehicle):
    """ concrete class to intantiate DMV manager object """

    parking_spots = []

    def assign_parking_spot(gate_number, parking_strategy):
        pass

@singelton
class LargeVehicle(IVehicle):
    """ concrete class to intantiate LargeVehicle manager object """

    parking_spots = []

    def assign_parking_spot(gate_number, parking_strategy):
        pass

class ParkingLotManager:
    """ Factory class for managing different types of vehicles """ 

    vehicle_object_mapping = {
        "two-wheeler": TwoWheeler(),
        "dmv": DMV(),
        "large-vehicle": LargeVehicle()
    }

    @staticmethod
    def assign_parking_area(vehicle_type):
        return ParkingLotManager.vehicle_object_mapping.get(vehicle_type, None)


class IPayment(metaclass=ABCMeta):
    """ Interface class for payment objects """

    @staticmethod
    @abstractmethod
    def make_payment():
        pass 

class PayPal(IPayment):

    def make_payment():
        pass 

class CreditCardPayment(IPayment):

    def make_payment():
        pass 

class PaymentFactory:
    """ factory class to intantiate payment-method object """

    payment_object_mapper = {
        "paypal": PayPalPayment(),
        "credit-card": CreditCardPayment()
    }

    @staticmethod
    def return_payment_object(payment_type):
        return PaymentFactory.return_payment_object.get(payment_type, None)


class IPaymentStrategy(metaclass=ABCMeta):
    pass

class HourlyPayment(IPaymentStrategy):
    pass 

class DailyPayment(IPaymentStrategy):
    pass 


class EntryGate:

    def __init__(self):
        self.gate_number = None 


class ExitGate:

    def __init__(self):
        self.gate_number = None 

class Entry:
    
    def __init__(Self):
        self.entry_gate_number = None 

class Exit:
    
    def __init__(Self):
        self.exit_gate_number = None 

class Ticket:

    def __init__(self, entry_gate, vehicle_type):
        self.gate_number = None 
        self.parking_time = None 
        self.parking_spot_id = None

    def generate_ticket(self):
        pass

class EntryManager:

    def enter(gate_number, vehicle_type, parking_strategy):
        parking_area = ParkingLotManager.assign_parking_area(vehicle_type=vehicle_type)
        parking_area.assign_parking_lot(gate_number, parking_strategy)

class ExitManager:
    
    def exit(gate_number, vehicle_type, parking_strategy):
        pass