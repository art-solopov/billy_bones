const path = require('path');
const process = require('process');

const gulp = require('gulp');
const sass = require('gulp-sass');

const appPaths = process.env['APP_PATHS'].split(':')
const assetPaths = appPaths.map( p => path.join(p, 'assets'))

gulp.task('css', () => {
    const scssPaths = assetPaths.map( p => path.join(p, 'css', '[a-z]*.scss'))
    return gulp.src(scssPaths)
	       .pipe(sass({
		   includePaths:[
		       // TODO add libraries here
		       ...assetPaths.map( p => path.join(p, 'shared'))
		   ]
	       }))
	       .pipe(gulp.dest(
		   f => {
		       let app = appPaths.find( x => f.path.startsWith(x) );
		       return path.normalize(path.join(app, 'static'))
		   }
	       ))
});
