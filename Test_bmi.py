import lab2.bmi as bmi

def test_bmi_normal_weight():
    result=bmi.calculate_bmi(60,1.7)
    assert(result==0)



    
def test_bmi_over_weight():
    result=bmi.calculate_bmi(100,1.7)
    assert(result==1)


    
def test_bmi_under_weight():
    result=bmi.calculate_bmi(40,1.7)
    assert(result==-1)

