"""
    @ 功能：ady16笔记：
    @ author：古城
"""

# # 读取文件操作类模板
# class ExcelHandler:
# 	def __init__(self,file_path):
# 		self.file_path = file_path
#
# 	def open_file(self):
# 		print("打开文件%s"%self.file_path)
#
# 	def get_sheet(self,name):
# 		self.open_file()
# 		print("获取表格%s"%name)
#
# 	def read_data(self,name):
# 		self.get_sheet(name)
# 		print("读取数据")
#
# 	def close(self):
# 		print("关闭文件：%s"%self.file_path)

# 解包 *[3,4,5,6] *（3,4,5,6）→等效于  3,4,5,6

# 封装对单元格的操作
import openpyxl


class ExcelHandler():

	def __init__(self,file_path):
		"""初始化对象"""
		self.file_path = file_path
		self.workbook = None
		self.sheet = None

	def open_file(self):
		"""作用：打开工作簿"""
		workbook = openpyxl.load_workbook(self.file_path)
		self.workbook = workbook
		print("————打开文件%s成功"%self.file_path)
		return workbook


	def get_sheet(self,sheet_name):
		"""作用：根据sheet名获取sheet"""
		workbook = self.open_file()
		sheet = workbook[sheet_name]
		self.sheet = sheet
		print("————获取表格%s中的%s成功"%(self.file_path,sheet_name))
		return sheet

	def read_data(self,sheet_name):
		"""根据Sheet名获取数据成字典元素的列表"""
		sheet = self.get_sheet(sheet_name)
		row_generator = sheet.rows

		test_data_dlist = []
		key_list = []
		for i, item in enumerate(row_generator):  # 遍历每行数据的元组
			if i == 0:  # 获取第一行取成字典元素的key列表
				for key_item in list(item):
					key_list.append(key_item.value)
			else:  # 根据key列表和后续行的数据组成一个字典，并把字典添加到数据列表里
				line_data = {}  # 用于接收数据构成数据列表中的字典元素
				for key, cell_data in zip(key_list, list(item)):
					line_data[key] = cell_data.value
				test_data_dlist.append(line_data)
		print("————读取%s中的%s中的数据成功"%(self.file_path,sheet_name))
		return test_data_dlist

	def write_data(self,sheet_name,row,column,data):
		"""将sheet_naem,单元格坐标（row,column)更新数据为data"""
		print("————更新%s的%s中单元格(%d,%d)的数据为%w"%(self.workbook,sheet_name,row,column,data))
		sheet = self.get_sheet(sheet_name)
		sheet.cell(row,column).value = data
		self.save()
		self.close()
		print("————数据写入成功")

	def save(self):
		self.workbook.close()

	def close(self):
		self.workbook.close()
		print("————关闭文件：%s"%self.file_path)



if __name__ == '__main__':
	excel = ExcelHandler("cases.xlsx")
	print(excel.read_data("Sheet1"))

"""ddt使用"""
# 1. 使用ddt.ddt装饰测试类
# 2. 使用ddt.data(*测试数据)装饰测试方法，并在测试方法加上接收测试数据的形参
