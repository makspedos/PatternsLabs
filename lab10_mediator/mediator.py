import datetime


class Mediator:
    def notify(self, sender, event:str):
        pass

class OrderMediator(Mediator):
    def __init__(self):
        self.date_range = None
        self.receive_checkbox = None
        self.deliver_selector = None

    def notify(self,sender, event:str):
        if sender == self.date_range and event == 'click':
            self.date_range.update_time()

        elif sender == self.receive_checkbox and event == 'checked':
            self.receive_checkbox.enable()
        elif sender == self.receive_checkbox and event == 'unchecked':
            self.receive_checkbox.disable()

        elif sender == self.deliver_selector and event == 'checked':
            self.deliver_selector.self_pickup = True
            self.date_range.set_visibility(False)
            self.receive_checkbox.change_state(False)

        elif sender == self.deliver_selector and event == 'unchecked':
            self.deliver_selector.self_pickup = False
            self.date_range.set_visibility(True)
            self.date_range.select_date(None)
            self.receive_checkbox.change_state(True)