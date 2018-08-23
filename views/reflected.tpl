% rebase('./views/base.tpl')
<h1>Reflected XSS</h1>

%if query == '':
<p>
  Search for something
</p>
%else:
<p>
  You've just searched for {{! query }}
</p>
%end

<form action="">
  <input name="q" type="text" value="{{ query }}"/>
  <button>Search!</button>
</form>
