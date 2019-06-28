"""
    作者：韩跃
    功能：计算空气质量指数
    日期：21/04/2019
    版本：9.0
    7.0新增功能：爬取网站所有城市的AQI信息并输出
    8.0新增功能：爬取网站所有城市的AQI信息并保存到数据表中
    9.0新增功能：对保存到数据表中的数据，分析指定列的最大值、最小值、均值
"""

import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('China_city_aqi_correct.csv')
    print(aqi_data.head(5))
    # print(aqi_data['City'])
    # print(aqi_data[['City', 'AQI']])
# 要拿到的是两栏元素组成的一个列表，需要在aqi_data[]中添加['City', 'AQI']
# 如果直接放入'City', 'AQI'，即print(aqi_data['City', 'AQI'])会出现报错提示

    print('基本信息：\n{}'.format(aqi_data.info))

    print('数据预览：\n{}'.format(aqi_data.head()))

    # 基本统计
    print('AQI最大值：', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI的均值：', aqi_data['AQI'].mean())


    # print(aqi_data['AQI'])
    # tuple = aqi_data['AQI'].apply(lambda x: eval(x)[1])  #.astype("float")
    # type(tuple)
    # print(type(tuple))
    # print('AQI的均值：', int(aqi_data['AQI']).mean())
    # print('AQI的均值：', tuple.mean())



    # top10
    # top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    # print('空气质量最好的10个城市为：{}'.format(top10_cities))
    # print(top10_cities)

    # bottom10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    # bottom10_cities = aqi_data.sort_values(by=['AQI'], encoding=False).head(10)
    # print('空气质量最差的十个城市为：{}'.format(bottom10_cities))
    # top10_cities.to_csv('top10_aqi.csv', index=False)
    # bottom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()


# import pandas as pd
#
#
# def main():
#     """
#         主函数
#     """
#     aqi_data1 = pd.read_csv('China_city_aqi1.csv')
#     aqi_data = pd.read_csv('china_city_aqi.csv')
#     print('基本信息：')
#     print(aqi_data.info())
#
#     print('数据预览：')
#     print(aqi_data.head())
#
#     # 基本统计
#     print('*******************')
#     print(aqi_data['AQI'])
#     print('*******************')
#     print(aqi_data1['AQI'])
#     print('********************')
#     # print('AQI最大值:', aqi_data['AQI'].max())
#     # print('AQI最小值：', aqi_data['AQI'].min())
#     # print('AQI均值：', aqi_data['AQI'].mean())
#
#     # top10
#     top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
#     print('空气质量最好的10个城市：')
#     print(top10_cities)
#
#     # bottom10
#     # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
#     bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
#     print('空气质量最差的10个城市：')
#     print(bottom10_cities)
#
#     # 保存csv文件
#     top10_cities.to_csv('top10_aqi.csv', index=False)
#     bottom10_cities.to_csv('bottom10_aqi.csv', index=False)
#
#
# if __name__ == '__main__':
#     main()
