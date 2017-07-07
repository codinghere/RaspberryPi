Taller de Raspberry
=================

<nav>
  <ul class="pagination">
    {% for post in site.posts  reversed %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{forloop.index}}</a></li>
    {% endfor %}
  </ul>
</nav>

# Tabla de contenidos

<ol>
  {% for post in site.posts  reversed %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li> 
  {% endfor %}
</ol>

<div class="posts">
  {% for post in paginator.posts %}
  <article class="post">
    <h1 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <!-- <time datetime="{{ post.date | date_to_xmlschema }}" class="post-date">{{ post.date | date_to_string }}</time> -->

    {{ post.content }}
  </article>
  {% endfor %}
</div>

TestX
=====
