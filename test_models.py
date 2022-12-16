from criptoexchange.models import AllCoinApiIO,Exchange,ModelError
from config import apiKey
import pytest
#16156 de  16378 (222)

def test_todocoin():
    todo = AllCoinApiIO()
    assert isinstance(todo, AllCoinApiIO)
    todo.getCoins(apiKey)
    assert len(todo.criptos) == 16156
    assert len(todo.no_criptos) == 222

def test_cambio_ok():
    cambio = Exchange("ETC")
    assert cambio.rate is None#True
    assert cambio.time is None#True
    cambio.updateExchange(apiKey)
    assert cambio.rate > 0
    assert isinstance(cambio.time,str)
    
def test_cambio_no_ok():
    noOk = Exchange("NADATEEWWQQQQ")
    #conseguir comparar Resultado de la clase ModelError, consultar como lo hicimos en romanos
    #assert noOk.updateExchange(apiKey) ==  ModelError( f"status: {noOk.r.status_code} error: {noOk.resultado['error']} ")
    
    with pytest.raises(ModelError) as exceptionInfo:
        noOk.updateExchange(apiKey)

    assert str(exceptionInfo.value) == "status: 550 error: You requested specific single item that we don't have at this moment. "    