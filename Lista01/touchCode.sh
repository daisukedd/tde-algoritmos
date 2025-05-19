#!/bin/bash

# Loop para criar arquivos de 23 até 53
for i in {23..53}
do
  # Criar o arquivo com o nome desejado
  touch "${i}code.py"
  echo "Arquivo ${i}code.py criado filhoo!"
done
