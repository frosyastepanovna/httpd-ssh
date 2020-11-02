import os

def process_GET():
    print ('<label for=fname>First name:</label><br><br><br><label for=fname>First name:</label>')
    #print('qq')
    
    print('''<form action="" method="post">
  <label for="host">host:</label><br>
  <input type="text" id="host" name="host"><br>
  <label for="login">login:</label><br>
  <input type="text" id="login" name="login"><br> 
  <label for="pass">pass:</label><br>
  <input type="password" id="pass" name="pass"><br>
  <label for="preexecute">preexecute:</label><br>
  <input type="text" id="preexecute" name="preexecute"><br>
  <input type="button" value="create" name="create" OnClick="b();">
  <input type="button" value="read" name="read" OnClick="a();">
  <input type="button" value="sync" name="sync" OnClick="b();">
  </form>''')
    
    return 0
    

