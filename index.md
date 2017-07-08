Taller de Raspberry
=================

# Tabla de contenidos

testing

<div id="post-nav">
    <div >    
        {% if page.previous.url %}
        <a class="prev" href="{{page.previous.url}}">
            <span>&lt; {{page.previous.title}}</span>
        </a> 
        {% endif %} 
        {% if page.next.url %} 
        <a class="next" href="{{page.next.url}}">
            <span>{{page.next.title}} &gt;</span>
        </a> 
        {% endif %} 
    </div>
</div>


<ol>
  {% for post in site.posts  reversed %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </li> 
  {% endfor %}
</ol>

