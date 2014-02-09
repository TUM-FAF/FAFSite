$ ->
  # Side navigation
  $sidenav = $('.sidenav')
  if $sidenav.length
    $subsidenavs = $sidenav.find('.subsidenav')

    # hide all subsidenavs
    $subsidenavs.addClass 'hide'
    # show subsidenav that contains active element
    $sidenav.find('.active').closest('.subsidenav').removeClass('hide')

    # hook subsidenavs opening when clicking on titles
    $sidenav.find('.title').on 'click', (ev)->
      $this = $(@)
      $subsidenavs.addClass 'hide'
      $this.siblings('.subsidenav').removeClass 'hide'

  # Table with details
  $('.table-with-details').each (index, value)->
    $(@).on 'click', '.btn[data-opener]', (ev)->
      $btn = $(@)
      $row = $btn.closest('tr')

      # Swap details with no-details
      if $row.hasClass('closed')
        $row.find('.no-details').hide()
        $row.find('.details').removeClass('hide').show()
      else
        $row.find('.details').hide()
        $row.find('.no-details').show()

      # Change button text
      alt_text = $btn.data('altText')
      $btn.data 'altText', $btn.text()
      $btn.text alt_text

      # Change row state
      $btn.closest('tr').toggleClass('closed opened')
