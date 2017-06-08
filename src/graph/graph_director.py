# Created by Simon Winder


class GraphDirector(object):
    def __init__(self, builder):
        self.__builder = builder

    def make_chart(self):
        self.__builder.get_data_for_chart()
        self.__builder.create_chart_structure()
        self.__builder.set_titles()
