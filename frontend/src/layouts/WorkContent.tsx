import React from 'react';
import {connect} from 'umi';
import styles from './WorkContent.less';

import Error404 from "./Error404";

const WorkContent: React.FC = (props: any) => {

  const {
    currentPage
  } = props;
  
  return (
    <div className={styles.container}>
      {
        (() => {
          switch (currentPage) {
            case 'note':
              return <Error404/>;
            case 'bookmark':
              return <Error404/>;
            default:
              return <Error404/>;
          }
        })()
      }
    </div>
  )
}

export default connect(({global}) => ({
  currentPage: global.currentPage
}))(WorkContent);