from profiler import profile

    
    # Normal Range        
def test_normal():
    result = profile(60, 100)
    assert result == "Normal"
def test_high():
    result = profile(101, 200)
    assert result == "High"   
def test_very_high():
    result = profile(201, 300)
    assert result == "Very High"       
def test_extremely_high():
    result = profile(301, 400)
    assert result == "Extremely High" 
    
    # Boundary minus one Range           
def test_less_than_normal():
    result = profile(59, 150)
    assert result != "Normal"    