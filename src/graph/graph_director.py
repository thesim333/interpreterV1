# Created by Simon Winder


class GraphDirector(object):
    def __init__(self, builder):
        self.builder = builder

    def make_chart(self):
        self.builder.get_data_for_chart()
        self.builder.create_chart_structure()
        self.builder.set_titles()
        self.builder.get_chart()
