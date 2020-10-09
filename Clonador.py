from urllib.request import urlretrieve
import os
from time import sleep

logo = r"""

   ******   **                                  **                  ****      **** 
  **////** /**                                 /**                 */// *    *///**
 **    //  /**  ******  *******   ******       /**  ******  ******/    /*   /*  */*
/**        /** **////**//**///** //////**   ****** **////**//**//*   ***    /* * /*
/**        /**/**   /** /**  /**  *******  **///**/**   /** /** /   *//     /**  /*
//**    ** /**/**   /** /**  /** **////** /**  /**/**   /** /**    *      **/*   /*
 //******  ***//******  ***  /**//********//******//****** /***   /******/**/ **** 
  //////  ///  //////  ///   //  ////////  //////  //////  ///    ////// //  ////  
                               -> @Created BY: hypn0thcy <-
                                          #AoGiri

"""

try:
    os.system('cls')
    print(logo)
    os.system('color')
    arq = input(" Link Da Página à Clonar -> ")
    frmt = input("\n  Formato? (EX: index.php) -> ")

    def download():
        urlretrieve(arq, frmt)

    download()
    os.system('cls')
    print(logo)
    os.system('color 0a')
    print('\n [...] -> Clonando... ')
    sleep(1.5)
    print("\n [!] PAGINA CLONADA COM SUCESSO! ARQUIVO -> {} [!]".format(frmt))
    exit()
except KeyboardInterrupt:
    os.system("cls")
    print(logo)
    os.system('color 5')
    print("\n                                        ^^Até mais!   ")
    exit()
except Exception as y:
    os.system('cls')
    print(logo)
    os.system('color 4')
    print('\n [...] -> Clonando... ')
    sleep(1)
    print('\n  [ERROR!] -> Houve algum erro! -> {}'.format(y))
    exit()
