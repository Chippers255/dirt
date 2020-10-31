class Analysis:

    def __init__(self):
        self.df = None
        self.shape = False
        self.mean = []
        self.median = []
        self.sum = []
        self.min = []
        self.max = []
    # end def __init__

    def from_df(self, df):
        self.df = df

        return self
    # end def from_df

    def select_shape(self):
        self.shape = True

        return self
    # end def select_shape

    def select_mean(self, column):
        self.mean.append(column)

        return self
    # end def select_mean

    def select_min(self, column):
        self.min.append(column)

        return self
    # end def select_min

    def select_max(self, column):
        self.max.append(column)

        return self
    # end def select_max

    def select_sum(self, column):
        self.sum.append(column)

        return self
    # end def select_sum

    def run(self):
        analysis = {}

        # If shape was asked for then calculate
        if self.shape:
            analysis["shape"] = self.df.shape

        # If 1 or more means where asked for then calculate
        if len(self.mean) > 0:
            analysis["mean"] = {}
            for i in self.mean:
                analysis["mean"][i] = self.df[i].mean()

        if len(self.min) > 0:
            analysis["min"] = {}
            for i in self.min:
                analysis["min"][i] = self.df[i].min()

        if len(self.max) > 0:
            analysis["max"] = {}
            for i in self.max:
                analysis["max"][i] = self.df[i].max()

        if len(self.sum) > 0:
            analysis["sum"] = {}
            for i in self.sum:
                analysis["sum"][i] = self.df[i].sum()

        return analysis
    # end def run

# end class Analysis
