from ast import In
from audioop import reverse
from curses.ascii import HT
from dataclasses import field
from urllib import request
from django.forms import ChoiceField
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
import numpy as np
import matplotlib.pyplot as plt
import io
from showapp.forms import MemberForm, InputForm, MF
from showapp.models import Information
from showapp.graph import Plot_Graph, batting_average_and_on_base_percentage, slugging_percentage
from datetime import date

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class InputView(FormView):
    template_name = "results.html"
    form_class = InputForm
    success_url = reverse_lazy("showapp:form")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DataView(ListView):
    model = Information
    context_object_name = "Information_list"
    template_name = 'data.html'
    
    def get_context_data(self, **kwargs):
        qs = Information.objects.all()
        id = [x.id for x in qs]
        mph = [x.mph for x in qs]
        plate_appearance = [x.plate_appearance for x in qs]
        #通算打率、OBP、SLG
        name1 = "Total Results"
        result = [x.result for x in qs]
        num = list(range(1,len(result)+1))
        avg, obp = batting_average_and_on_base_percentage(result)
        slg = slugging_percentage(result)
        #対右
        name2 = "vsR Results"
        right_result = [x.result for x in qs if x.hand =="右"]
        right_num = list(range(1,len(right_result)+1))
        avg_vr, obp_vr = batting_average_and_on_base_percentage(right_result)
        slg_vr = slugging_percentage(right_result)
        #対左
        name3 = "vsL Results"
        left_result = [x.result for x in qs if x.hand =="左"]
        left_num = list(range(1,len(left_result)+1))
        avg_vl, obp_vl = batting_average_and_on_base_percentage(left_result)
        slg_vl = slugging_percentage(left_result)
        #球種ごとstraight
        name4 = "vsStraight Results"
        result_straight = [x.result for x in qs if x.ball_type=="4-seam-fastball" or x.ball_type=="2-seam-fastball"]
        num_straight = list(range(1, len(result_straight)+1))
        avg_straight, obp_straight = batting_average_and_on_base_percentage(result_straight)
        slg_straight = slugging_percentage(result_straight)
        #slider
        name5 = "vsSlider Results"
        result_slider = [x.result for x in qs if x.ball_type=="slider"]
        num_slider = list(range(1, len(result_slider)+1))
        avg_slider, obp_slider = batting_average_and_on_base_percentage(result_slider)
        slg_slider = slugging_percentage(result_slider)
        #Cut
        name6 = "vsCut Results"
        result_cut = [x.result for x in qs if x.ball_type=="cut"]
        num_cut = list(range(1, len(result_cut)+1))
        avg_cut, obp_cut = batting_average_and_on_base_percentage(result_cut)
        slg_cut = slugging_percentage(result_cut)
        #Curve
        name7 = "vsCurve Results"
        result_curve = [x.result for x in qs if x.ball_type=="curve"]
        num_curve = list(range(1, len(result_curve)+1))
        avg_curve, obp_curve = batting_average_and_on_base_percentage(result_curve)
        slg_curve = slugging_percentage(result_curve)
        #Sinker
        name8 = "vsSinker Results"
        result_sinker = [x.result for x in qs if x.ball_type=="sinker"]
        num_sinker = list(range(1, len(result_sinker)+1))
        avg_sinker, obp_sinker = batting_average_and_on_base_percentage(result_sinker)
        slg_sinker = slugging_percentage(result_sinker)
        #Sinker
        name9 = "vsChangeUp Results"
        result_changeup = [x.result for x in qs if x.ball_type=="change-up"]
        num_changeup = list(range(1, len(result_changeup)+1))
        avg_changeup, obp_changeup = batting_average_and_on_base_percentage(result_changeup)
        slg_changeup = slugging_percentage(result_changeup)
        #Splitter
        name9 = "vsSplitter Results"
        result_splitter = [x.result for x in qs if x.ball_type=="splitter"]
        num_splitter = list(range(1, len(result_splitter)+1))
        avg_splitter, obp_splitter = batting_average_and_on_base_percentage(result_splitter)
        slg_splitter = slugging_percentage(result_splitter)
        #今日の打率
        name10 = "Today Results"
        result_today = [x.result for x in qs if x.date==date.today()]
        num_today = list(range(1, len(result_today)+1))
        avg_today, obp_today = batting_average_and_on_base_percentage(result_today)
        slg_today = slugging_percentage(result_today)
        #plate_appearance1
        name11 = "First at bat"
        result_fat = [x.result for x in qs if x.plate_appearance=="1"]
        num_fat = list(range(1, len(result_fat)+1))
        avg_fat, obp_fat = batting_average_and_on_base_percentage(result_fat)
        slg_fat = slugging_percentage(result_fat)
        #plate_appearance2
        name12 = "Second at bat"
        result_sat = [x.result for x in qs if x.plate_appearance=="2"]
        num_sat = list(range(1, len(result_sat)+1))
        avg_sat, obp_sat = batting_average_and_on_base_percentage(result_sat)
        slg_sat = slugging_percentage(result_sat)
        #plate_appearance3
        name13 = "Third at bat"
        result_tat = [x.result for x in qs if x.plate_appearance=="3"]
        num_tat = list(range(1, len(result_tat)+1))
        avg_tat, obp_tat = batting_average_and_on_base_percentage(result_tat)
        slg_tat = slugging_percentage(result_tat)
        #plate_appearance4
        name14 = "Fourth at bat"
        result_foat = [x.result for x in qs if x.plate_appearance=="4"]
        num_foat = list(range(1, len(result_foat)+1))
        avg_foat, obp_foat = batting_average_and_on_base_percentage(result_foat)
        slg_foat = slugging_percentage(result_foat)
        #plate_appearance5~
        name15 = "After the fifth at bat"
        result_afat = [x.result for x in qs if x.plate_appearance=="5" or x.plate_appearance=="6" or x.plate_appearance=="7"]
        num_afat = list(range(1, len(result_afat)+1))
        avg_afat, obp_afat = batting_average_and_on_base_percentage(result_afat)
        slg_afat = slugging_percentage(result_afat)
        #no runner
        name16 = "no runner"
        result_nr = [x.result for x in qs if x.first_runner==False and x.second_runner==False and x.third_runner==False] 
        num_nr = list(range(1, len(result_nr)+1))
        avg_nr, obp_nr = batting_average_and_on_base_percentage(result_nr)
        slg_nr = slugging_percentage(result_nr)
        #first runner
        name17 = "only on first runner"
        result_fb = [x.result for x in qs if x.first_runner and x.second_runner==False and x.third_runner==False] 
        num_fb = list(range(1, len(result_fb)+1))
        avg_fb, obp_fb = batting_average_and_on_base_percentage(result_fb)
        slg_fb = slugging_percentage(result_fb)
        #second runner
        name18 = "only on second runner"
        result_sb = [x.result for x in qs if x.first_runner==False and x.second_runner and x.third_runner==False] 
        num_sb = list(range(1, len(result_sb)+1))
        avg_sb, obp_sb = batting_average_and_on_base_percentage(result_sb)
        slg_sb = slugging_percentage(result_sb)
        #first runner
        name19 = "only on third runner"
        result_tb = [x.result for x in qs if x.first_runner==False and x.second_runner==False and x.third_runner] 
        num_tb = list(range(1, len(result_tb)+1))
        avg_tb, obp_tb = batting_average_and_on_base_percentage(result_tb)
        slg_tb = slugging_percentage(result_tb)
        #first and second runner
        name20 = "on first and second runner"
        result_fsb = [x.result for x in qs if x.first_runner and x.second_runner and x.third_runner==False] 
        num_fsb = list(range(1, len(result_fsb)+1))
        avg_fsb, obp_fsb = batting_average_and_on_base_percentage(result_fsb)
        slg_fsb = slugging_percentage(result_fsb)
        #first and third runner
        name21 = "on first and third runner"
        result_ftb = [x.result for x in qs if x.first_runner and x.second_runner==False and x.third_runner] 
        num_ftb = list(range(1, len(result_ftb)+1))
        avg_ftb, obp_ftb = batting_average_and_on_base_percentage(result_ftb)
        slg_ftb = slugging_percentage(result_ftb)
        #second and third runner
        name22 = "on second and third runner"
        result_stb = [x.result for x in qs if x.first_runner==False and x.second_runner and x.third_runner] 
        num_stb = list(range(1, len(result_stb)+1))
        avg_stb, obp_stb = batting_average_and_on_base_percentage(result_stb)
        slg_stb = slugging_percentage(result_stb)
        #full base runner
        name23 = "on full base runner"
        result_fbr = [x.result for x in qs if x.first_runner and x.second_runner and x.third_runner] 
        num_fbr = list(range(1, len(result_fbr)+1))
        avg_fbr, obp_fbr = batting_average_and_on_base_percentage(result_fbr)
        slg_fbr = slugging_percentage(result_fbr)
        #season
        name24 = "2023"
        result_2023 = [x.result for x in qs if x.season=="2023"] 
        num_2023 = list(range(1, len(result_2023)+1))
        avg_2023, obp_2023 = batting_average_and_on_base_percentage(result_2023)
        slg_2023 = slugging_percentage(result_2023)             


        chart1 = Plot_Graph(num, avg, obp, slg, name1)
        chart2 = Plot_Graph(right_num, avg_vr, obp_vr, slg_vr, name2)
        chart3 = Plot_Graph(left_num, avg_vl, obp_vl, slg_vl, name3)
        chart4 = Plot_Graph(num_straight, avg_straight, obp_straight, slg_straight, name4)
        chart5 = Plot_Graph(num_slider, avg_slider, obp_slider, slg_slider, name5)
        chart6 = Plot_Graph(num_cut, avg_cut, obp_cut, slg_cut, name6)
        chart7 = Plot_Graph(num_curve, avg_curve, obp_curve, slg_curve, name7)
        chart8 = Plot_Graph(num_changeup, avg_changeup, obp_changeup, slg_changeup, name8)
        chart9 = Plot_Graph(num_splitter, avg_splitter, obp_splitter, slg_splitter, name9)
        chart10 = Plot_Graph(num_today, avg_today, obp_today, slg_today, name10)
        chart11 = Plot_Graph(num_fat, avg_fat, obp_fat, slg_fat, name11)
        chart12 = Plot_Graph(num_sat, avg_sat, obp_sat, slg_sat, name12)
        chart13 = Plot_Graph(num_tat, avg_tat, obp_tat, slg_tat, name13)
        chart14 = Plot_Graph(num_foat, avg_foat, obp_foat, slg_foat, name14)
        chart15 = Plot_Graph(num_afat, avg_afat, obp_afat, slg_afat, name15)
        chart16 = Plot_Graph(num_nr, avg_nr, obp_nr, slg_nr, name16)
        chart17 = Plot_Graph(num_fb, avg_fb, obp_fb, slg_fb, name17)
        chart18 = Plot_Graph(num_sb, avg_sb, obp_sb, slg_sb, name18)
        chart19 = Plot_Graph(num_tb, avg_tb, obp_tb, slg_tb, name19)
        chart20 = Plot_Graph(num_fsb, avg_fsb, obp_fsb, slg_fsb, name20)
        chart21 = Plot_Graph(num_ftb, avg_ftb, obp_ftb, slg_ftb, name21)
        chart22 = Plot_Graph(num_stb, avg_stb, obp_stb, slg_stb, name22)
        chart23 = Plot_Graph(num_fbr, avg_fbr, obp_fbr, slg_fbr, name23)
        chart24 = Plot_Graph(num_2023, avg_2023, obp_2023, slg_2023, name24)

        context = super().get_context_data(**kwargs)
        context["chart1"] = chart1
        context["chart2"] = chart2
        context["chart3"] = chart3
        context["chart4"] = chart4
        context["chart5"] = chart5
        context["chart6"] = chart6
        context["chart7"] = chart7
        context["chart8"] = chart8
        context["chart9"] = chart9
        context["chart10"] = chart10
        context["chart11"] = chart11
        context["chart12"] = chart12
        context["chart13"] = chart13
        context["chart14"] = chart14
        context["chart15"] = chart15
        context["chart16"] = chart16
        context["chart17"] = chart17
        context["chart18"] = chart18
        context["chart19"] = chart19
        context["chart20"] = chart20
        context["chart21"] = chart21
        context["chart22"] = chart22
        context["chart23"] = chart23
        context["chart24"] = chart24
        return context