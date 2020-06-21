from get_data import Get_data
import execution

#爬取网站数据，进行解析
data = Get_data()
data.get_data()
time_in,time_out = data.get_time()
data.parse_data()

#根据解析得到的数据，进行分析出各种分布图和旅游负因子分布图
execution.china_map(time_in)
execution.province_map(time_in)
execution.china_travel_map(time_in)