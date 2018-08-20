% rebase('./static/base.tpl')
<h1>Persistent XSS</h1>

<ol>
  %for (user, message) in messages:
  <li><strong>{{! user }}</strong> {{! message }}</li>
  %end
</ol>

<form action="" method="POST">
  <input name="user" autocomplete="off" type="text" value="{{ last_user }}"/>
  <input name="message" autocomplete="off" type="text" value="" autofocus />
  <button>Send!</button>
</form>
