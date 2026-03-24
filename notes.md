---
title: "Notes"
layout: post
permalink: /notes/
---
{% for post in site.notes %}
  <article class="post-entry">
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
  </article>
{% endfor %}

