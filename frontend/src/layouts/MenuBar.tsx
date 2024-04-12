import React from "react";
import {connect} from 'umi';
import {Tooltip} from "antd";
import {Icons} from 'aird';
import styles from './MenuBar.less';

const MenuBar: React.FC = (props: any) => {

  const {
    dispatch,
    layoutSize,
    frameSize,
    currentPage
  } = props;

  const handleClickMenuItem = (id: string) => {
    dispatch({
      type: 'global/changeCurrentPage',
      payload: id
    });
    // 触发窗口resize事件
    window.dispatchEvent(new Event('resize'));
  }

  const menuItems = [
    {
      id: 'note',
      title: '文案',
      icon: 'wiki',
      role: 'user'
    },
    {
      id: 'tool',
      title: '工具',
      icon: 'tool',
      role: 'user'
    },
  ];

  return (
    <div className={styles.container} style={{height: frameSize.height, width: layoutSize.menuWidth, top: 0, left: 0}}>
      {
        menuItems.map(item => {
          return (
            <Tooltip placement="right" title={item.title} mouseEnterDelay={0.2} mouseLeaveDelay={0}
                     destroyTooltipOnHide={true} overlayInnerStyle={{fontSize: 13, fontWeight: 600, borderRadius: 3}}
                     key={item.id}
            >
              <div key={item.id} className={styles.menu} onClick={() => handleClickMenuItem(item.id)}>
                <div className={styles.icon} style={{width: layoutSize.menuWidth, height: layoutSize.menuWidth + 5}}>
                  {
                    currentPage === item.id ?
                      <div className={styles.selected}/> : null
                  }
                  <Icons name={item.icon} size={22} thickness={1.5}/>
                </div>
              </div>
            </Tooltip>
          )
        })
      }
      <div className={styles.bottomButtons}>
        <Tooltip placement="right" title={'设置'} mouseEnterDelay={0.2} mouseLeaveDelay={0}
                     destroyTooltipOnHide={true} overlayInnerStyle={{fontSize: 13, fontWeight: 600, borderRadius: 3}}
                     key={'setting'}
            >
              <div key={'setting'} className={styles.menu} onClick={() => handleClickMenuItem('setting')}>
                <div className={styles.icon} style={{width: layoutSize.menuWidth, height: layoutSize.menuWidth + 5}}>
                  {
                    currentPage === 'setting' ?
                      <div className={styles.selected}/> : null
                  }
                  <Icons name={'settings'} size={22} thickness={1.5}/>
                </div>
              </div>
            </Tooltip>
      </div>
    </div>
  );
}

export default connect(({global}) => ({
  currentPage: global.currentPage,
  frameSize: global.frameSize,
  layoutSize: global.layoutSize
}))(MenuBar);
