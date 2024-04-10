import React, {useEffect} from "react";
import { connect } from 'umi';
import {ConfigProvider, message} from 'antd';
import MenuBar from "./MenuBar";
import WorkContent from "./WorkContent";

import '../global.less';

const BasicLayout: React.FC = (props: any) => {

  const {
    dispatch
  } = props;
  
  const handleWindowResize = () => {
    dispatch({
      type: 'global/changeFrameSize'
    });
  }

  useEffect(() => {
    handleWindowResize();

    message.config({
      top: 0,
      duration: 1,
      maxCount: 1,
      prefixCls: 'air',
      rtl: false,
    });

    // 监听窗口尺寸变化事件
    window.addEventListener('resize', handleWindowResize);

    return () => {
      // 移除监听
      window.removeEventListener('resize', handleWindowResize);
    };
  }, []);

  return (
    <ConfigProvider
      prefixCls="air"
    >
      <MenuBar />
      <WorkContent />
    </ConfigProvider>
  );
}

export default connect(({global}) => ({
  global
}))(BasicLayout);