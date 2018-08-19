% rebase('./static/base.tpl')
<h1>Hello!</h1>

<p>
  This is just a welcome page, please head to intended example:
</p>

<ul>
  %for uri, name in examples.items():
  <li>
    <a href="{{ uri }}">{{ name }}</a>
  </li>
  %end
</ul>
