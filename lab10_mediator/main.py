from mediator import OrderMediator
from component import DateComponent, ReceiverCheckbox, PickUpButton



if __name__ == '__main__':
    mediator = OrderMediator()

    date_picker = DateComponent(mediator)
    receiver_checkbox = ReceiverCheckbox(mediator)
    pickup_button = PickUpButton(mediator)

    mediator.date_range = date_picker
    mediator.receive_checkbox = receiver_checkbox
    mediator.deliver_selector = pickup_button

    date_picker.select_date('01.11.2024')
    receiver_checkbox.change_state(True)

    pickup_button.set_self_pickup(True)
    pickup_button.set_self_pickup(False)
