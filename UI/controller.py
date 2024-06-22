import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.graph = None

    def handleAnalizzaOggetti(self, e):
        self._view.txt_result.clean()
        self.graph = self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f'Numero nodi: {len(self.graph.nodes)}\nNumero archi: {len(self.graph.edges)}'))
        self._view.update_page()
    def handleCompConnessa(self,e):
        idObj = self._view._txtIdOggetto.value
        if idObj == '':
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text(f'INSERISCI UN ID VALIDO!!!!'))
            self._view.update_page()
            return
        if int(idObj) in self._model.idMap.keys():
            self._view.txt_result.clean()
            connessa = self._model.componenteConnessa(int(idObj))
            self._view.txt_result.controls.append(ft.Text(f'Numero nodi connessi: {len(connessa)}'))
            self._view.update_page()
        else:
            print('++++++')
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text(f'INSERISCI UN ID VALIDO!!!!'))
            self._view.update_page()
            return

