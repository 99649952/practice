# -*-coding:utf-8-*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Q
import models
import re
import operator

search_list = ['192.168.10.1', '商城节点', 80, '配置高',] # 模糊查询返回请求，顺序和个数可以随意
accurately_search = {'ip': '1.1.1.1', 'port': 80, 'hostname': '商城节点1',}  # 精确查询请求


class Search(object):
    def __init__(self, hostname=None, ip=None, port=None,description=None):
        self.hostname = hostname
        self.ip = ip
        self.port = port
        self.description = description
        self.Q_dict = {
            'ip__exact': self.ip,
            'hostname__exact': self.hostname,
            'port__exact': self.port,
            'description__exact': self.description}    # 返回的结果用于精确匹配

    def handle(self, query_list):   # 返回的字典用于模糊匹配
        query_result = {}
        contact_list = []
        pattern = re.compile(r'([12]?\d{1,2}\.){3}([12]?\d{1,2})')  #判断是否是ip
        for query in query_list:
            try:
                if pattern.search(query) is not None:
                    query_result['ip'] = query
                elif type(query) is int:    #是int就是端口
                    query_result['port'] = query
                else:   #其他为描述或节点名
                    contact_list.append(query)
            except TypeError:
                pass
        query_result['contact'] = contact_list
        self.Q_dict = query_result
        return query_result

    def matching_contains(self):    #处理模糊匹配
        query_list = []
        for matching_contains in ['hostname__contains', 'description__contains']:#节点和描述模糊匹配
            for vlaue in self.Q_dict.get('contact'):
                q_obj = Q(**{matching_contains: vlaue})
                query_list.append(q_obj)
        matching_exact_list = [Q(**{'ip__exact': self.Q_dict.get('ip')}), Q(**{'port__exact': self.Q_dict.get('port')})] \
        #这个地方可以写活。 ip和端口精确匹配
        for matching_exact in matching_exact_list:
            query_list.append(matching_exact)
        return query_list

    def matching_exact(self):
        del_list = []
        for i in self.Q_dict:
            if self.Q_dict[i] is None:
                del_list.append(i)
        for del_i in del_list:
            del self.Q_dict[del_i]  #将None搜索去掉
        print(self.Q_dict)
        q_obj = Q(**self.Q_dict)
        return q_obj


def query_or(request): #处理or查询
    query_obj = Search()
    query_obj.handle(search_list)
    query_list = query_obj.matching_contains()
    queryset = models.Host.objects.filter(reduce(operator.or_, query_list))
    print (queryset)
    return HttpResponse('ok')


def query_and(request): #处理and查询
    query_obj = Search(ip=accurately_search.get('ip'), hostname=accurately_search.get('hostname'),
                       port=accurately_search.get('port'), description=accurately_search.get('description'))
    query_dict = query_obj.matching_exact()
    queryset = models.Host.objects.filter(query_dict)
    print(queryset)
    return HttpResponse('exact')
