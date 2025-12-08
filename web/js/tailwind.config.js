// tailwind.config.js
module.exports = {
    theme: {
      extend: {
        animation: {
          fadeInRight: 'fadeInRight 1s ease-out forwards',
          fadeInLeft: 'fadeInLeft 1s ease-out forwards',
        },
        keyframes: {
          fadeInRight: {
            '0%': { opacity: '0', transform: 'translateX(20px)' },
            '100%': { opacity: '1', transform: 'translateX(0)' },
          },
          fadeInLeft: {
            '0%': { opacity: '0', transform: 'translateX(-20px)' },
            '100%': { opacity: '1', transform: 'translateX(0)' },
          },
          fontfamily:{
            akaya :['akaya Teliviga']
          }
          
          
        },
        
      },
    },
    plugins: [],
  };

  // tailwind.config.js
module.exports = {
  theme: {
    extend: {
      keyframes: {
        slideInFromLeft: {
          '0%': { transform: 'translateX(-100%)', opacity: 0 },
          '100%': { transform: 'translateX(0)', opacity: 1 },
        },
        slideInFromRight: {
          '0%': { transform: 'translateX(100%)', opacity: 0 },
          '100%': { transform: 'translateX(0)', opacity: 1 },
        },
      },
      animation: {
        slideInFromLeft: 'slideInFromLeft 1s ease-out forwards',
        slideInFromRight: 'slideInFromRight 1s ease-out forwards',
      },
    },
  },
  plugins: [],
};

  
  