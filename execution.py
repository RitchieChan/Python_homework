import map_draw
import json
map = map_draw.Draw_map()
# 格式
# map.to_map_china(['湖北'],['99999'],'1584201600')
# map.to_map_city(['荆门市'],['99999'],'湖北','1584201600')

# 获取数据
with open('data.json', 'r') as file:
    data = file.read()
    data = json.loads(data)

# 中国疫情地图
def  china_map(update_time):
    area = []
    confirmed = []
    curConfirm=[]
    for each in data:
        curConfirm.append(each['curConfirm'])
        area.append(each['area'])
        confirmed.append(each['confirmed'])
    map.to_map_china(area,confirmed,update_time,curConfirm)

# 23个省、5个自治区、4个直辖市、2个特别行政区 香港、澳门和台湾的subList为空列表，未有详情数据

# 省、直辖市疫情地图
def province_map(update_time):
    for each in data:
        city = []
        confirmeds = []
        curConfirm=[]
        province = each['area']
        for each_city in each['subList']:
            curConfirm.append(each['curConfirm'])
            city.append(each_city['city']+"市")
            confirmeds.append(each_city['confirmed'])
            map.to_map_city(city,confirmeds,province,update_time,curConfirm)
        if province == '上海' or '北京' or '天津' or '重庆':
            for each_city in each['subList']:
                city.append(each_city['city'])
                confirmeds.append(each_city['confirmed'])
                map.to_map_city(city,confirmeds,province,update_time,curConfirm)
                
def china_travel_map(update_time):
    
    #旅游疫情因子
    travel_factor=[]
    
    total_confirmed=0
    total_curConfirm=0
    area = []
    confirmed = []
    curConfirm=[]
    for each in data:
        total_curConfirm=total_curConfirm+float(each['curConfirm'])
        total_confirmed=total_confirmed+float(each['confirmed'])    
    avr_confirmed=total_confirmed/len(data)
    avr_curConfirm=total_curConfirm/len(data)
    for each in data:
        curConfirm.append(each['curConfirm'])
        area.append(each['area'])
        confirmed.append(each['confirmed'])
        #factor=(float(each['curConfirm'])-avr_curConfirm)*0.1+(float(each['confirmed'])-avr_confirmed)*10
        #可见，因子越高，风险越高
        factor=float(each['curConfirm'])*0.1+float(each['confirmed'])*10
        travel_factor.append(factor)
    
    #直接借用to_map_china函数，避免代码重复，特此说明
    map.to_map_china_travel(area,travel_factor,update_time)