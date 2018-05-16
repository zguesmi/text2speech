module.exports = {
  name: 'text2speech',
  app: {
    type: 'DOCKER',
    envvars: 'XWDOCKERIMAGE=ziedguesmi/text2speech',
  },
  work: {
    cmdline: '',
    dirinuri: 'https://github.com/Zied-Guesmi/text2speech/blob/master/DATADIR.zip?raw=true'
  }
};
