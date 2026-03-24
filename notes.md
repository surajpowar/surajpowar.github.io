---
title: "Notes"
layout: post
permalink: /notes/
---
{% for post in site.notes %}
  <article class="post-entry">
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p>{{ post.date | date: "%B %d, %Y" }}</p>
  </article>
{% endfor %}

