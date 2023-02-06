module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: 'media', // or 'media' or 'class'
  theme: {
    fontFamily: {
      sans: ['Plus Jakarta Sans', 'sans-serif']
    },
    extend: {
      backgroundImage: {
        // left as an example:
        // 'join': "url('assets/images/join-bg.svg')"
      },
      boxShadow: {
        lg: '0 -2px 15px -3px rgba(0, 0, 0, 0.2), 0 4px 6px -2px rgba(0, 0, 0, 0.05)'
      },
      colors: {
        fwxBlack: '#101128',
        fwxBackgroundWhite: '#fafafa'
      },
      fontSize: {
        'tiny': '0.6rem'
      }
    },
  },
  variants: {
    extend: {
    },
  },
  plugins: [],
}
