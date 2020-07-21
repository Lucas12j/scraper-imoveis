# Scraper-Imóveis


## Atenção:

A chamada da classe que coleta os dados no site Zap foi comentada na classe graph_int, devido a mudanças na forma em que o site agora envia os parâmetros relacionados
ao tamanho do imóvel.

Posteriormente atualizarei com um novo formador de url resolvendo esse problema.

Caso necessite utilizar tal classe, ainda é possível. Basta não passar nada nos campos de tamanho máximo ou tamanho mínimo.

### Preparando o Ambiente: 

É importante ressaltar que usei o Geckodriver para realizar buscas automaticas no Firefox neste projeto, logo é necessário ter instalado tanto um como o outro na máquina.  

```
pip install -r requirements.txt
```

### Por fim execute a classe main:

``` 
python main.py
