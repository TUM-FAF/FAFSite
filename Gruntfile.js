'use strict';

module.exports = function(grunt) {
  // load all grunt tasks
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  // configurable paths
  var fruitConfig = {
    src: 'src',
    mockup: 'mockup',
    app: 'app'
  };

  // Project configuration
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    fruit: fruitConfig,
    watch: {
      stylus: {
        files: ['<%= fruit.src %>/style/{,*/}*.styl'],
        tasks: ['stylus:development'],
        options: {
          nospawn: true,
          livereload: true
        }
      },
      coffee: {
        files: ['<%= fruit.src %>/script/{,*/}*.coffee'],
        tasks: ['coffee:development'],
        options: {
          nospawn: true,
          livereload: true
        }
      },
      template: {
        files: ['<%= fruit.src %>/template/{,*/}*.hbs', '<%= fruit.src %>/template/data/data.json'],
        tasks: ['template'],
        options: {
          nospawn: true,
          livereload: true
        }
      },
      development: {
        options: {
          nospawn: true,
          livereload: true
        },
        files: [
          '<%= fruit.mockup %>/{,*/}*.html',
          '<%= fruit.mockup %>/{,*/}*.css',
          '<%= fruit.mockup %>/{,*/}*.js',
          '<%= fruit.mockup %>/{,*/}*.{png,jpg,jpeg,gif}'
        ],
        tasks: []
      }
    },
    stylus: {
      development: {
        options: {
          urlfunc: 'embedurl', // use embedurl('test.png') in our code to trigger Data URI embedding
          compress: false,
          linenos: true
        },
        files: {
          '<%= fruit.mockup %>/css/application.css': '<%= fruit.src %>/style/*.build.styl' // compile and concat into single file
        }
      },
      production: {
        options: {
          urlfunc: 'embedurl'
        },
        files: {
          '<%= fruit.mockup %>/css/application.css': '<%= fruit.src %>/style/*.build.styl'
        }
      }
    },
    coffee: {
      development: {
        options: {
          sourceMap: true,
          bare: true
        },
        files: [{
          expand: true,
          cwd: '<%= fruit.src %>/script',
          src: '*.coffee',
          dest: '<%= fruit.mockup %>/js',
          ext: '.js'
        }]
      },
      production: {
        options: {
          bare: true,
          join: true
        },
        files: {
          '<%= fruit.mockup %>/js/application.js': '<%= fruit.src %>/script/*.coffee' // concat then compile into single file
        }
      }
    },
    template: {
      all: {
        engine: 'handlebars',
        cwd: '<%= fruit.src %>/template/',
        partials: ['<%= fruit.src %>/template/partials/*.hbs'],
        data: '<%= fruit.src %>/template/data/data.json',
        options: {
        },
        files: [
          {
            expand: true,     // Enable dynamic expansion.
            cwd: '<%= fruit.src %>/template/',      // Src matches are relative to this path.
            src: '*.hbs', // Actual pattern(s) to match.
            dest: '<%= fruit.mockup %>/',   // Destination path prefix.
            ext: '.html'  // Dest filepaths will have this extension.
          }
        ]
      }
    },
    clean: {
      production: {
        src: ['<%= fruit.mockup %>/js/*.map']
      }
    }
  });

  grunt.registerTask('build', [
    'stylus:production',
    'coffee:production',
    'template',
    'clean:production'
  ]);

  grunt.registerTask('server', [
    'stylus:development',
    'coffee:development',
    'watch'
  ]);

  grunt.registerTask('default', [
    'server'
  ]);

};
