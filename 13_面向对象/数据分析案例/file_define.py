"""
和文件相关的类定义
"""
from data_define import Record

# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:
        """ 读取文件的数据，读到的每一条数据都转换为 Record 对象，将它们都封装到 list 内返回即可"""
        pass


class CsvFileReader(FileReader):

    def __init__(self, path) -> None:
        self.path = path    # 定义成员变量记录文件的路径


    # 复写(实现抽象方法)父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip() # leading and trailing whitespace removed
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    csv_file_reader = CsvFileReader("/workspaces/pythontest/13_面向对象/数据分析案例/2011年1月销售数据.txt")
    csv_file_reader.read_data()