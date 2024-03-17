from pyspark import SparkContext

def main():
    sc = SparkContext(appName='SparkVisibility')

    input_file = sc.textFile('/user/hadoop/input_project_q2/*-99999-*')
    station_vdist = input_file.filter(lambda line: line[78:84] != '999999' and line[84:85] in ['0','1','4','5','9']) \
                              .map(lambda line: (line[4:10], (int(line[78:84]), 1))) \
                              .reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1])) \
                              .map(lambda x: (x[0], x[1][0]/x[1][1]))
    station_vdist.saveAsTextFile('/user/hadoop/outputdata/output_project_q2.txt')

    sc.stop()

if __name__ == '__main__':
    main()
