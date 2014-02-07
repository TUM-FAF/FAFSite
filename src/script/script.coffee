$ ->
  $sidenav = $('.sidenav')
  if $sidenav.length
    $subsidenavs = $sidenav.find('.subsidenav')
    if $sidenav.find('.active').length
      # hide all subsidenavs
      $subsidenavs.addClass 'hide'
      # show subsidenav that contains active element
      $sidenav.find('.active').closest('.subsidenav').removeClass('hide')

      # hook subsidenavs opening when clicking on titles
      $sidenav.find('.title').on 'click', (ev)->
        $this = $(@)
        $subsidenavs.addClass 'hide'
        $this.siblings('.subsidenav').removeClass 'hide'
