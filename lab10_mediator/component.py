from mediator import Mediator


class Component:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator


class DateComponent(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)
        self.selected_date = None
        self.visible = True

    def select_date(self, date):
        self.selected_date = date
        self.mediator.notify(self, 'click')


    def update_time(self):
        print(f'Time updated based on date: {self.selected_date}')

    def set_visibility(self, visible: bool):
        self.visible = visible

class ReceiverCheckbox(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator=mediator)
        self.name = None
        self.phone = None
        self.outsider_receiver = False

    def change_state(self, state: bool):
        self.outsider_receiver = state
        if self.outsider_receiver:
            self.mediator.notify(self, 'checked')
        else:
            self.mediator.notify(self, 'unchecked')


    def enable(self):
        print('Name and phone enabled')

    def disable(self):
        print('Name and phone disabled')


class PickUpButton(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator=mediator)
        self.self_pickup = False

    def set_self_pickup(self, self_pickup: bool):
        if self_pickup:
            self.mediator.notify(self, 'checked')
        else:
            self.mediator.notify(self, 'unchecked')
