import openpyxl

class ExcelHandler:
	def __init__(self,file_path):
		self.file_path = file_path
		self.workbook = None

	def open_file(self):
		"""打开excel，返回workbook"""
		workbook = openpyxl.load_workbook(self.file_path)
		self.workbook = workbook
		return workbook

	def get_sheet(self,sheet_name):
		"""根据工作表名返回文件file_path的sheet"""
		workbook = self.open_file()
		print("获取表格%s"%sheet_name)
		return workbook[sheet_name]

	def read_data(self,sheet_name):
		"""以字典元素的列表返回指定工作表中的数据"""
		print("读取%s中%s中的数据"%(self.file_path,sheet_name))
		sheet = self.get_sheet(sheet_name)
		row_generator = sheet.rows

		test_data_dlist = []
		key_list = []
		# for i, item in enumerate(row_generator):  # 遍历每行数据的元组
		# 	if i == 0:  # 获取第一行取成字典元素的key列表
		# 		for key_item in list(item):
		# 			key_list.append(key_item.value)
		# 	else:  # 根据key列表和后续行的数据组成一个字典，并把字典添加到数据列表里
		# 		line_data = {}  # 用于接收数据构成数据列表中的字典元素
		# 		for key, cell_data in zip(key_list, list(item)):
		# 			line_data[key] = cell_data.value
		# 		test_data_dlist.append(line_data)
		# print("————读取%s中的%s中的数据成功" % (self.file_path, sheet_name))
		for i,item in enumerate(list(row_generator)):
			print(i,item)
			if i == 0:
				for x in item:
					key_list.append(x.value)
			else:
				line_data = {}
				for i,x in enumerate(item):
					line_data[key_list[i]]=x.value
				test_data_dlist.append(line_data)
		return test_data_dlist


	def save(self):
		self.workbook.save()

	def close(self):
		print("关闭文件：%s"%self.file_path)


if __name__ == '__main__':
	ExcelHandler("cases.xlsx").read_data("Sheet1")