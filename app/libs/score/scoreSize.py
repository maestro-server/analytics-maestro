class ScoreSize(object):
    mindex = [2, 2.5, 3.5, 7, 11, 22, 46, 76, 1000]
    mvalue = ['nano', 'micro', 'small', 'medium', 'large', '2xlarge', '4xlarge', '8xlarge', '8xlarge']

    @staticmethod
    def scored(scr):
        valued = None

        for key, val in zip(ScoreSize.mindex, ScoreSize.mvalue):
            if scr <= key:
                valued = val
                break

        return valued