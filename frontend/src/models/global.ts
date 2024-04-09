export default {
  namespace: 'global',
  state: {
    layoutSize: {
      headerHeight: 0,
      menuWidth: 40
    },
    // 工作区框架尺寸
    frameSize: {
      width: 0,
      height: 0
    },
    currentPage: 'note',
  },
  effects: {},
  reducers: {
    changeFrameSize(state: any, _: any) {
      const frameWidth = window.innerWidth - state.layoutSize.menuWidth;
      const frameHeight = window.innerHeight - state.layoutSize.headerHeight;

      return {
        ...state,
        frameSize: {
          width: frameWidth,
          height: frameHeight
        }
      }
    },

    changeCurrentPage(state: any, action: any) {
      return {
        ...state,
        currentPage: action.payload
      }
    }
  },
};