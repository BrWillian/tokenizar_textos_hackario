stopwords = ['a', 'à', 'agora', 'ainda', 'alguém', 'algum', 'alguma', 'algumas', 'alguns', 'ampla', 'amplas', 'amplo', 'amplos', 'ante', 'antes', 'ao', 'aos', 'após', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'até', 'através', 'cada', 'coisa', 'coisas', 'com', 'como', 'contra', 'contudo', 'da', 'daquele', 'daqueles', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'dessa', 'dessas', 'desse', 'desses', 'desta', 'destas', 'deste', 'deste', 'destes', 'deve', 'devem', 'devendo', 'dever', 'deverá', 'deverão', 'deveria', 'deveriam', 'devia', 'deviam', 'disse', 'disso', 'disto', 'dito', 'diz', 'dizem', 'do', 'dos', 'e', 'é', "e'", 'ela', 'elas', 'ele', 'eles', 'em', 'enquanto', 'entre', 'era', 'essa', 'essas', 'esse', 'esses', 'esta', 'está', 'estamos', 'estão', 'estas', 'estava', 'estavam', 'estávamos', 'este', 'estes', 'estou', 'eu', 'fazendo', 'fazer', 'feita', 'feitas', 'feito', 'feitos', 'foi', 'for', 'foram', 'fosse', 'fossem', 'grande', 'grandes', 'há', 'isso', 'isto', 'já', 'la', 'la', 'lá', 'lhe', 'lhes', 'lo', 'mas', 'me', 'mesma', 'mesmas', 'mesmo', 'mesmos', 'meu', 'meus', 'minha', 'minhas', 'muita', 'muitas', 'muito', 'muitos', 'na', 'não', 'nas', 'nem', 'nenhum', 'nessa', 'nessas', 'nesta', 'nestas', 'ninguém', 'no', 'nos', 'nós', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'nunca', 'o', 'os', 'ou', 'outra', 'outras', 'outro', 'outros', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'pequena', 'pequenas', 'pequeno', 'pequenos', 'per', 'perante', 'pode', 'pôde', 'podendo', 'poder', 'poderia', 'poderiam', 'podia', 'podiam', 'pois', 'por', 'porém', 'porque', 'posso', 'pouca', 'poucas', 'pouco', 'poucos', 'primeiro', 'primeiros', 'própria', 'próprias', 'próprio', 'próprios', 'quais', 'qual', 'quando', 'quanto', 'quantos', 'que', 'quem', 'são', 'se', 'seja', 'sejam', 'sem', 'sempre', 'sendo', 'será', 'serão', 'seu', 'seus', 'si', 'sido', 'só', 'sob', 'sobre', 'sua', 'suas', 'talvez', 'também', 'tampouco', 'te', 'tem', 'tendo', 'tenha', 'ter', 'teu', 'teus', 'ti', 'tido', 'tinha', 'tinham', 'toda', 'todas', 'todavia', 'todo', 'todos', 'tu', 'tua', 'tuas', 'tudo', 'última', 'últimas', 'último', 'últimos', 'um', 'uma', 'umas', 'uns', 'vendo', 'ver', 'vez', 'vindo', 'vir', 'vos', 'vós', 'a', 'about', 'above', 'according', 'across', 'actually', 'after', 'again', 'against', 'all', 'almost', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anything', 'are', 'aren', 'as', 'at', 'away', 'back', 'back', 'be', 'because', 'been', 'before', 'behind', 'being', 'below', 'besides', 'better', 'between', 'beyond', 'both', 'but', 'by', 'can', 'certain', 'could', 'do', 'does', 'during', 'each', 'else', 'enough', 'even', 'ever', 'few', 'for', 'from', 'further', 'get', 'going', 'got', 'great', 'has', 'have', 'he', 'her', 'here', 'high', 'his', 'how', 'however', 'i', 'if', 'in', 'instead', 'into', 'is', 'it', 'its', 'itself', 'just', 'later', 'least', 'less', 'less', 'let', 'little', 'many', 'may', 'maybe', 'me', 'might', 'more', 'most', 'much', 'must', 'neither', 'never', 'new', 'no', 'non', 'nor', 'not', 'nothing', 'of', 'off', 'often', 'old', 'on', 'once', 'one', 'only', 'or', 'other', 'our', 'out', 'over', 'perhaps', 'put', 'rather', 'really', 'set', 'several', 'she', 'should', 'since', 'snot', 'snt', 'so', 'some', 'something', 'sometimes', 'soon', 'still', 'such', 't', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'this', 'those', 'though', 'three', 'through', 'till', 'to', 'together', 'too', 'toward', 'towards', 'two', 'under', 'up', 'upon', 'us', 'very', 'very', 'was', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'whole', 'whose', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'a', 'acá', 'adelante', 'además', 'ahí', 'ahora', 'al', 'alguna', 'algunas', 'alguno', 'algunos', 'as', 'así', 'aún', 'bastante', 'bien', 'cada', 'como', 'con', 'cosa', 'cosas', 'cual', 'cuál', 'cuales', 'cuáles', 'cuando', 'da', 'de', 'debe', 'debemos', 'del', 'dentro', 'desde', 'después', 'donde', 'dos', 'durante', 'e', 'el', 'ellos', 'en', 'entonces', 'entre', 'era', 'eran', 'es', 'esa', 'esas', 'ese', 'eso', 'esos', 'esta', 'está', 'estaba', 'estaban', 'estamos', 'están', 'estar', 'estas', 'este', 'esto', 'estos', 'frente', 'fue', 'fuera', 'fueron', 'ha', 'haber', 'había', 'hace', 'hacen', 'hacer', 'hacia', 'haciendo', 'han', 'hasta', 'hay', 'hecho', 'hoy', 'la', 'las', 'le', 'les', 'lo', 'los', 'me', 'mientras', 'misma', 'mismas', 'mismo', 'mismos', 'mucha', 'muchas', 'mucho', 'muchos', 'muy', 'ni', 'no', 'nos', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'o', 'ó', 'os', 'otra', 'otras', 'otro', 'otros', 'para', 'pero', 'podemos', 'podría', 'por', 'porque', 'puede', 'pueden', 'pues', 'que', 'qué', 'se', 'sea', 'según', 'segundo', 'ser', 'sería', 'si', 'sido', 'siendo', 'sobre', 'solamente', 'son', 'su', 'tal', 'tambíen', 'tan', 'tanto', 'tenemos', 'tener', 'tenían', 'tiene', 'tienen', 'toda', 'todas', 'todavía', 'todo', 'todos', 'través', 'un', 'una', 'uno', 'va', 'vamos', 'van', 'veces', 'vemos', 'ver', 'vez', 'y', 'ya']