
def media_mcginley(df, periods:list):
    '''
        A Média Dinâmica McGinley é um tipo de média móvel que foi projetada para acompanhar o mercado melhor do que os indicadores de média móvel existentes.
        É um indicador técnico que melhora as linhas médias móveis,ajustando-se para mudanças na velocidade do mercado. John R. McGinley,
        um técnico de mercado, é o inventor do indicador homônimo.

        INPUTS
        df: dataframe com dados de fechamentos
        periods: lista contendo médias a serem calculadas
    '''

    for period in periods:
        df[f'McGinley_{period}'] = 0
        for i in range(len(df)):
            if df[f'McGinley_{period}'].iloc[i-1]==0:
                df[f'McGinley_{period}'].iloc[i] = df['Adj Close'].iloc[i]
            else:
                df[f'McGinley_{period}'].iloc[i] = (df[f'McGinley_{period}'].iloc[i-1]
                                                        +(df['Adj Close'].iloc[i] - df[f'McGinley_{period}'].iloc[i-1])
                                                        /(0.6*period*(df['Adj Close'].iloc[i]/df[f'McGinley_{period}'].iloc[i-1])**4))
    return df