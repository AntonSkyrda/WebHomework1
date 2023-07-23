import abc


class AbstractUI(abc.ABC):

    @abc.abstractmethod
    def display_contacts(self, contacts):
        pass

    @abc.abstractmethod
    def display_search_results(self, results):
        pass

    @abc.abstractmethod
    def show_message(self, message):
        pass

    @abc.abstractmethod
    def get_user_input(self, prompt):
        pass
