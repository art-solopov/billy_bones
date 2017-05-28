const path = require('path');
const env = require('process').env;

const webpack = require('webpack');

const ExtractTextPlugin = require('extract-text-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');
const _ = require('lodash');

const dist = path.resolve(__dirname, 'home/static/');

function moduleName(format) {
    let name = '[name]';
    if(env.WEBPACK_PRODUCTION) {
	name += '-[chunkhash]';
    }
    return `${name}.${format}`;
}

module.exports = {
    entry: {
	application: ['babel-polyfill', './assets/js/index.js', './assets/css/index.css']
    },
    output: {
	filename: moduleName('js'),
	path: dist
    },
    module: {
	rules: [
	    {
		test: /\.(css|less)$/,
		use: ExtractTextPlugin.extract({
		    fallback: 'style-loader',
		    use: ['css-loader', 'less-loader']
		})
	    },
	    {
		test: /\.js$/,
		exclude: /(node_modules|bower_components)/,
		use: {
		    loader: 'babel-loader',
		    options: {
			presets: ['env']
		    }
		}
	    },
	    {
		test: /\.(jpeg|png|gif|svg|eot|ttf|woff|woff2)$/i,
		use: [{
		    loader: 'file-loader',
		    options: {
			dist,
			name: env.WEBPACK_PRODUCTION ? '[name]-[hash].[ext]' : '[name].[ext]',
			publicPath: env.WEBPACK_PRODUCTION ? '/static/' : 'http://localhost:12800/'
		    }
		}]

	    }
	]
    },
    plugins: [
	new ExtractTextPlugin(moduleName('css')),
	new webpack.ProvidePlugin({
	    $: 'jquery',
	    jQuery: 'jquery',
	    tether: 'tether',
	    Tether: 'tether'
	}),
	new webpack.optimize.CommonsChunkPlugin(
	    {
		name: 'vendor',
		minChunks: module => module.context && _.includes(module.context, 'node_modules')
		
	    }
	),
	new webpack.optimize.CommonsChunkPlugin({name: 'runtime'}),
	new ManifestPlugin()
    ],
    devServer: {
	contentBase: dist,
	compress: true,
	port: 12800
    }
};
