// db = Database("bolt://44.211.161.134:7687", "neo4j", "threshold-population-divider")
// Limpa o banco de dados
MATCH (n) DETACH DELETE n;

// Cria as Cidades
CREATE (:City {name: "Rio de Janeiro"});
CREATE (:City {name: "São Paulo"});
CREATE (:City {name: "Belo Horizonte"});
CREATE (:City {name: "Porto Alegre"});
CREATE (:City {name: "Fortaleza"});

// Cria os times
CREATE (:Team {name: "Flamengo"});
CREATE (:Team {name: "Fluminense"});
CREATE (:Team {name: "Vasco da Gama"});
CREATE (:Team {name: "Botafogo"});
CREATE (:Team {name: "São Paulo"});
CREATE (:Team {name: "Palmeiras"});
CREATE (:Team {name: "Corinthians"});
CREATE (:Team {name: "Cruzeiro"});
CREATE (:Team {name: "Atlético Mineiro"});
CREATE (:Team {name: "Internacional"});
CREATE (:Team {name: "Grêmio"});
CREATE (:Team {name: "Fortaleza"});

// Associa os times as cidades
MATCH (t:Team {name: "Flamengo"}), (c:City {name: "Rio de Janeiro"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Fluminense"}), (c:City {name: "Rio de Janeiro"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Vasco da Gama"}), (c:City {name: "Rio de Janeiro"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Botafogo"}), (c:City {name: "Rio de Janeiro"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "São Paulo"}), (c:City {name: "São Paulo"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Palmeiras"}), (c:City {name: "São Paulo"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Corinthians"}), (c:City {name: "São Paulo"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Cruzeiro"}), (c:City {name: "Belo Horizonte"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Atlético Mineiro"}), (c:City {name: "Belo Horizonte"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Internacional"}), (c:City {name: "Porto Alegre"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Grêmio"}), (c:City {name: "Porto Alegre"})
CREATE (t)-[:FROM_City]->(c);
MATCH (t:Team {name: "Fortaleza"}), (c:City {name: "Fortaleza"})
CREATE (t)-[:FROM_City]->(c);

// Cria os estádios
CREATE (:Stadium {name: "Maracanã", City: "Rio de Janeiro"});
CREATE (:Stadium {name: "São Januário", City: "Rio de Janeiro"});
CREATE (:Stadium {name: "Nilton Santos", City: "Rio de Janeiro"});
CREATE (:Stadium {name: "Morumbi", City: "São Paulo"});
CREATE (:Stadium {name: "Allianz Parque", City: "São Paulo"});
CREATE (:Stadium {name: "Neo Química", City: "São Paulo"});
CREATE (:Stadium {name: "Mineirão", City: "Belo Horizonte"});
CREATE (:Stadium {name: "MRV", City: "Belo Horizonte"});
CREATE (:Stadium {name: "Beira Rio", City: "Porto Alegre"});
CREATE (:Stadium {name: "Arena do Grêmio", City: "Porto Alegre"});
CREATE (:Stadium {name: "Castelão", City: "Fortaleza"});

// Associa os estádios as cidades
MATCH (s:Stadium {name: "Maracanã"}), (c:City {name: "Rio de Janeiro"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "São Januário"}), (c:City {name: "Rio de Janeiro"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Nilton Santos"}), (c:City {name: "Rio de Janeiro"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Morumbi"}), (c:City {name: "São Paulo"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Allianz Parque"}), (c:City {name: "São Paulo"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Neo Química"}), (c:City {name: "São Paulo"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Mineirão"}), (c:City {name: "Belo Horizonte"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "MRV"}), (c:City {name: "Belo Horizonte"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Beira Rio"}), (c:City {name: "Porto Alegre"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Arena do Grêmio"}), (c:City {name: "Porto Alegre"})
CREATE (s)-[:LOCATED_IN]->(c);
MATCH (s:Stadium {name: "Castelão"}), (c:City {name: "Fortaleza"})
CREATE (s)-[:LOCATED_IN]->(c);

// Associa os times aos estádios
MATCH (t:Team {name: "Flamengo"}), (s:Stadium {name: "Maracanã"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Fluminense"}), (s:Stadium {name: "Maracanã"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Vasco da Gama"}), (s:Stadium {name: "São Januário"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Botafogo"}), (s:Stadium {name: "Nilton Santos"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "São Paulo"}), (s:Stadium {name: "Morumbi"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Palmeiras"}), (s:Stadium {name: "Allianz Parque"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Corinthians"}), (s:Stadium {name: "Neo Química"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Cruzeiro"}), (s:Stadium {name: "Mineirão"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Atlético Mineiro"}), (s:Stadium {name: "MRV"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Internacional"}), (s:Stadium {name: "Beira Rio"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Grêmio"}), (s:Stadium {name: "Arena do Grêmio"})
CREATE (t)-[:PLAYS_IN]->(s);
MATCH (t:Team {name: "Fortaleza"}), (s:Stadium {name: "Castelão"})
CREATE (t)-[:PLAYS_IN]->(s);

// Cria as partidas
MATCH (t1:Team {name: "Flamengo"}), (t2:Team {name: "Corinthians"})
CREATE (m1:Match {date: "2024-11-30", score: "2-1"})-[:HOME_TEAM]->(t1),
       (m1)-[:AWAY_TEAM]->(t2);

MATCH (t1:Team {name: "Atlético Mineiro"}), (t2:Team {name: "Grêmio"})
CREATE (m2:Match {date: "2024-11-30", score: "1-3"})-[:HOME_TEAM]->(t1),
       (m2)-[:AWAY_TEAM]->(t2);

MATCH (t1:Team {name: "Cruzeiro"}), (t2:Team {name: "Vasco da Gama"})
CREATE (m3:Match {date: "2024-11-30", score: "1-0"})-[:HOME_TEAM]->(t1),
       (m3)-[:AWAY_TEAM]->(t2);

MATCH (t1:Team {name: "Internacional"}), (t2:Team {name: "Botafogo"})
CREATE (m4:Match {date: "2024-11-30", score: "2-3"})-[:HOME_TEAM]->(t1),
       (m4)-[:AWAY_TEAM]->(t2);

MATCH (t1:Team {name: "Palmeiras"}), (t2:Team {name: "São Paulo"})
CREATE (m5:Match {date: "2024-11-30", score: "2-4"})-[:HOME_TEAM]->(t1),
       (m5)-[:AWAY_TEAM]->(t2);

MATCH (t1:Team {name: "Fortaleza"}), (t2:Team {name: "Fluminense"})
CREATE (m6:Match {date: "2024-11-30", score: "2-0"})-[:HOME_TEAM]->(t1),
       (m6)-[:AWAY_TEAM]->(t2);

// Cria as rivalidades
MATCH (t1:Team {name: "Flamengo"}), (t2:Team {name: "Vasco da Gama"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Flamengo"}), (t2:Team {name: "Fluminense"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Flamengo"}), (t2:Team {name: "Botafogo"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Vasco da Gama"}), (t2:Team {name: "Botafogo"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Fluminense"}), (t2:Team {name: "Vasco da Gama"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Fluminense"}), (t2:Team {name: "Botafogo"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Palmeiras"}), (t2:Team {name: "Corinthians"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Palmeiras"}), (t2:Team {name: "São Paulo"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "São Paulo"}), (t2:Team {name: "Corinthians"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Cruzeiro"}), (t2:Team {name: "Atlético Mineiro"})
CREATE (t1)-[:RIVAL_OF]->(t2);

MATCH (t1:Team {name: "Internacional"}), (t2:Team {name: "Grêmio"})
CREATE (t1)-[:RIVAL_OF]->(t2);

// Cria os técnicos
MERGE (c1:Coach {name: "Filipe Luís"})
WITH c1
MATCH (t:Team {name: "Flamengo"})
CREATE (c1)-[:COACHES]->(t);

MERGE (c2:Coach {name: "Felipe Maestro"})
WITH c2
MATCH (t:Team {name: "Vasco da Gama"})
CREATE (c2)-[:COACHES]->(t);

MERGE (c3:Coach {name: "Artur Jorge"})
WITH c3
MATCH (t:Team {name: "Botafogo"})
CREATE (c3)-[:COACHES]->(t);

MERGE (c4:Coach {name: "Abel Ferreira"})
WITH c4
MATCH (t:Team {name: "Palmeiras"})
CREATE (c4)-[:COACHES]->(t);

MERGE (c5:Coach {name: "Ramón Díaz"})
WITH c5
MATCH (t:Team {name: "Corinthians"})
CREATE (c5)-[:COACHES]->(t);

MERGE (c6:Coach {name: "Luis Zubeldía"})
WITH c6
MATCH (t:Team {name: "São Paulo"})
CREATE (c6)-[:COACHES]->(t);

MERGE (c7:Coach {name: "Fernando Diniz"})
WITH c7
MATCH (t:Team {name: "Cruzeiro"})
CREATE (c7)-[:COACHES]->(t);

MERGE (c8:Coach {name: "Gabriel Milito"})
WITH c8
MATCH (t:Team {name: "Atlético Mineiro"})
CREATE (c8)-[:COACHES]->(t);

MERGE (c9:Coach {name: "Roger Machado"})
WITH c9
MATCH (t:Team {name: "Internacional"})
CREATE (c9)-[:COACHES]->(t);

MERGE (c10:Coach {name: "Renato Portaluppi"})
WITH c10
MATCH (t:Team {name: "Grêmio"})
CREATE (c10)-[:COACHES]->(t);

MERGE (c11:Coach {name: "Vojvoda"})
WITH c11
MATCH (t:Team {name: "Fortaleza"})
CREATE (c11)-[:COACHES]->(t);

MERGE (c12:Coach {name: "Mano Menezes"})
WITH c12
MATCH (t:Team {name: "Fluminense"})
CREATE (c12)-[:COACHES]->(t);

// Cria os jogadores
CREATE (:Player {name: "Arrascaeta", position: "Meio-campo"});
CREATE (:Player {name: "Bruno Henrique", position: "Atacante"});
CREATE (:Player {name: "Hulk", position: "Atacante"});
CREATE (:Player {name: "Everton Ribeiro", position: "Meio-campo"});
CREATE (:Player {name: "Gustavo Gómez", position: "Zagueiro"});
CREATE (:Player {name: "Matheus Pereira", position: "Meio-campo"});
CREATE (:Player {name: "Memphis Depay", position: "Atacante"});
CREATE (:Player {name: "Enner Valencia", position: "Atacante"});
CREATE (:Player {name: "Arboleda", position: "Zagueiro"});
CREATE (:Player {name: "Igor Gomes", position: "Meio-campo"});
CREATE (:Player {name: "Pikachu", position: "Meio-campo"});
CREATE (:Player {name: "Lucas Lima", position: "Meio-campo"});
CREATE (:Player {name: "Marchesín", position: "Goleiro"});
CREATE (:Player {name: "Luiz Henrique", position: "Meio-campo"});
CREATE (:Player {name: "Fábio", position: "Goleiro"});
CREATE (:Player {name: "Philippe Coutinho", position: "Meio-campo"});

// Associa os jogadores aos times
MATCH (p:Player {name: "Arrascaeta"}), (t:Team {name: "Flamengo"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Bruno Henrique"}), (t:Team {name: "Flamengo"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Hulk"}), (t:Team {name: "Atlético Mineiro"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Gustavo Gómez"}), (t:Team {name: "Palmeiras"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Matheus Pereira"}), (t:Team {name: "Cruzeiro"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Memphis Depay"}), (t:Team {name: "Corinthians"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Enner Valencia"}), (t:Team {name: "Internacional"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Arboleda"}), (t:Team {name: "São Paulo"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Igor Gomes"}), (t:Team {name: "São Paulo"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Pikachu"}), (t:Team {name: "Fortaleza"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Lucas Lima"}), (t:Team {name: "Fortaleza"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Marchesín"}), (t:Team {name: "Grêmio"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Luiz Henrique"}), (t:Team {name: "Botafogo"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Fábio"}), (t:Team {name: "Fluminense"})
CREATE (p)-[:PLAYS_FOR]->(t);
MATCH (p:Player {name: "Philippe Coutinho"}), (t:Team {name: "Vasco da Gama"})
CREATE (p)-[:PLAYS_FOR]->(t);

// Adiciona FanGroups organizadas
CREATE (:FanGroup {name: "Raça Rubro-Negra"});
CREATE (:FanGroup {name: "Gaviões da Fiel"});
CREATE (:FanGroup {name: "Mancha Verde"});
CREATE (:FanGroup {name: "Geral do Grêmio"});
CREATE (:FanGroup {name: "Leões da TUF"});
CREATE (:FanGroup {name: "Galoucura"});
CREATE (:FanGroup {name: "Máfia Azul"});

// Relaciona FanGroups organizadas aos times
MATCH (f:FanGroup {name: "Raça Rubro-Negra"}), (t:Team {name: "Flamengo"})
CREATE (f)-[:SUPPORTS]->(t);
MATCH (f:FanGroup {name: "Gaviões da Fiel"}), (t:Team {name: "Corinthians"})
CREATE (f)-[:SUPPORTS]->(t);
MATCH (f:FanGroup {name: "Mancha Verde"}), (t:Team {name: "Palmeiras"})
CREATE (f)-[:SUPPORTS]->(t);
MATCH (f:FanGroup {name: "Geral do Grêmio"}), (t:Team {name: "Grêmio"})
CREATE (f)-[:SUPPORTS]->(t);
MATCH (f:FanGroup {name: "Leões da TUF"}), (t:Team {name: "Fortaleza"})
CREATE (f)-[:SUPPORTS]->(t);
MATCH (f:FanGroup {name: "Galoucura"}), (t:Team {name: "Atlético Mineiro"})
CREATE (f)-[:SUPPORTS]->(t);
MATCH (f:FanGroup {name: "Máfia Azul"}), (t:Team {name: "Cruzeiro"})
CREATE (f)-[:SUPPORTS]->(t);
