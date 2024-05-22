import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handelAnalizza(self, e):
        nMin = self._view._txtInNumC.value
        self._model.buildGraph(int(nMin))

    def handleConnessi(self, e):
        pass

    def handleTestConnessione(self, e):
        pass

    def handleCercaItinerario(self, e):
        pass