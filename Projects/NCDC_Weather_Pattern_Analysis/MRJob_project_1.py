from mrjob.job import MRJob

class MRMaxTemp(MRJob):
    def mapper(self, _, line):
        input = line.strip()
        (month, heights, quality) = (input[19:21], input[70:75], input[75:76])
        if(heights != '99999' and quality in ['0','1','4','5','9']):
            yield(month, heights)

    def reducer(self, month, heights):
        hmax = 0
        hmin = next(heights)
        for i in heights:
            if(i>hmax):
                hmax=i
            if(i<hmin):
                hmin=i
        hrange = int(hmax)-int(hmin)
        yield(month, hrange)

if __name__ == '__main__':
    MRMaxTemp.run()
